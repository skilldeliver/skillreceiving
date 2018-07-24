#!/usr/bin/python
#
# by Erik Osheim
#
# This program uses a recursive descent, LL1 parser to generate a Code object
# for the given input. Code objects are pure expressions whose behavior can
# only be controlled via a dictionary of strings-to-numbers provided to run.
#
# Syntax:
#
# * decimal numbers (e.g. 3, 4.52)
# * simple names (foo, qux13).
# * built-in constants: pi, e, i
# * arithmetic operators: + - * / % // ^ !
# * parenthesis and absolute value: (2 + 3) * |4 - x|
# * built-in functions:
#   abs, ceil, cos, degrees, floor, log, log10,
#   log2, max, min, radians, round, sin, tan
#
# You can test this program out on the command-line. For instance:
#
#   python calc.py "2 + 2"
#
#   python calc.py "9!"
#
#   python calc.py "2^foo - 1" foo=8
#
#   python calc.py "e^(i*pi) + 1"

import math
import re
import sys
import time

# private expression cache
_cache = {}

# public methods
def prepare(s):
    "Prepare the given expression 's' and return a Code object."
    global _cache
    if s not in _cache:
        _cache[s] = Code.gen(Parser(s).parse())
    return _cache[s]

def run(s, d):
    "Run the given expression 's' using the variables from 'd'."
    return prepare(s).run(d)

def flush():
    "Clear the expression cache."
    global _cache
    _cache = {}

# everything below here is semi-private, except the Code class, which is
# returned from prepare().
class Lexeme(object):
    def __init__(self, name, pos, data):
        self.name = name
        self.pos = pos
        self.data = data
    def __repr__(self):
        return 'Lexeme(%r, %d, %r)' % (self.name, self.pos, self.data)

class Lexer(object):
    num_re = re.compile(r'(?:0|[1-9][0-9]*)(?:\.[0-9]+)?')

    def __init__(self, data):
        self.data = data
        self.lexs = []

    def lexid(self, i):
        j = i + 1
        while j < len(self.data) and self.data[j].isalnum(): j += 1
        self.lexs.append(Lexeme('id', i, self.data[i:j]))
        return j

    def lexnum(self, i):
        j = i + 1
        while j < len(self.data) and self.data[j].isdigit(): j += 1
        k = j
        if k < len(self.data) and self.data[k] == '.':
            k += 1
            while k < len(self.data) and self.data[k].isdigit(): k += 1
        if k > j + 1:
            self.lexs.append(Lexeme('num', i, self.data[i:k]))
            return k
        else:
            self.lexs.append(Lexeme('num', i, self.data[i:j]))
            return j

    def lex(self):
        i = 0
        while i < len(self.data):
            c = self.data[i]
            if c.isspace():
                i += 1
            elif c.isalpha():
                i = self.lexid(i)
            elif c.isdigit():
                i = self.lexnum(i)
            elif c == '/' and self.data[i:i + 2] == '//':
                self.lexs.append(Lexeme('//', i, '//'))
                i += 2
            else:
                self.lexs.append(Lexeme(c, i, c))
                i += 1
        self.lexs.append(Lexeme('$', i, None))
        return self.lexs

class Expr(object):
    def __init__(self, op, *args):
        self.op = op
        self.args = args
    def __repr__(self):
        return 'Expr(%r, %r)' % (self.op, self.args)

    def lisp(self):
        if self.op == 'num':
            return self.args[0]
        elif self.op == 'id':
            return self.args[0]
        elif self.op == 'apply':
            return '(%s %s)' % (self.args[0], ' '.join([a.lisp() for a in self.args[1:]]))
        elif self.args:
            return '(%s %s)' % (self.op, ' '.join([a.lisp() for a in self.args]))
        else:
            return self.op

class Parser(object):
    debug = False

    def error(self):
        if self.debug:
            raise Exception("parse error at %r" % self.cur)
        else:
            raise Exception("parse error at %r (byte %d)" % (self.cur.data, self.cur.pos))

    def __init__(self, data):
        self.lexer = Lexer(data)

    def next(self):
        self.k += 1
        self.cur = self.lexs[self.k]

    def parse(self):
        self.k = 0
        self.lexs = self.lexer.lex()
        self.cur = self.lexs[0]
        return self.parseP()

    def lxin(self, names):
        return self.cur.name in names

    pnames = set(['num', 'id', '(', '|', '-'])
    def parseP(self):
        return self.parseE1()

    def parseEx(self, names, f1, f2, right=False):
        lhs = f1()
        lst = f2()
        if not lst:
            return lhs
        elif right:
            lst = [lhs] + lst
            expr = lst[-1]
            i = len(lst) - 3
            while i >= 0:
                expr = Expr(lst[i + 1], lst[i], expr)
                i -= 2
            return expr
        else:
            expr = lhs
            i = 0
            while i < len(lst) - 1:
                expr = Expr(lst[i], expr, lst[i + 1])
                i += 2
            return expr
    
    def parseE1(self):
        return self.parseEx(self.pnames, self.parseE2, self.parseE1_)

    def parseE2(self):
        return self.parseEx(self.pnames, self.parseE3, self.parseE2_)

    dash = set(['-'])
    e3names = set(['num', 'id', '(', '|'])
    def parseE3(self):
        if self.cur.name == '-':
            self.next()
            expr = self.parseE3()
            return Expr('-', expr)
        else:
            return self.parseE4()

    def parseE4(self):
        return self.parseEx(self.e3names, self.parseE5, self.parseE4_, right=True)

    def parseE5(self):
        expr = self.parseE6()
        if self.parseE5_() is None:
            return expr
        else:
            return Expr('!', expr)

    lpar = set(['('])
    pipe = set(['|'])
    rpar = set([')'])
    def parseE6(self):
        c = self.cur
        if c.name == 'num':
            self.next()
            return Expr('num', c.data)
        elif c.name == 'id':
            self.next()
            a = self.parseA()
            if a is None:
                return Expr('id', c.data)
            else:
                return Expr('apply', c.data, *a)
        elif c.name == '(':
            self.next()
            e1 = self.parseE1()
            if self.lxin(self.rpar):
                self.next()
                return e1
            else:
                self.error()
        elif c.name == '|':
            self.next()
            e1 = self.parseE1()
            if self.lxin(self.pipe):
                self.next()
                return Expr('abs', e1)
            else:
                self.error()
        else:
            self.error()

    anames = set(['!', '$', '^', '*', '/', '//', '%', '+', '-', ')', '|', ','])
    def parseA(self):
        if self.lxin(self.lpar):
            self.next()
            ll = self.parseL()
            if self.lxin(self.rpar):
                self.next()
                return ll
            else:
                self.error()
        else:
            return None

    lnames = set(['num', 'id', '(', '|', '-'])
    def parseL(self):
        e1 = self.parseE1()
        l_ = self.parseL_()
        if l_ is None:
            return [e1]
        else:
            return [e1] + l_

    comma = set([','])
    def parseL_(self):
        if self.lxin(self.comma):
            self.next()
            e1 = self.parseE1()
            l_ = self.parseL_()
            if l_ is None:
                return [e1]
            else:
                return [e1] + l_
        else:
            return None

    def parseEx_(self, names, skips, f1):
        if self.lxin(names):
            c = self.cur
            self.next()
            lhs = f1()
            lst = self.parseEx_(names, skips, f1)
            return [c.name, lhs] + lst
        else:
            return []

    e1_names = set(['+', '-'])
    e1_skips = set([')', '|', ',', '$'])
    def parseE1_(self):
        return self.parseEx_(self.e1_names, self.e1_skips, self.parseE2)

    e2_names = set(['*', '/', '//', '%'])
    e2_skips = set(['+', '-', '$', ')', '|', ','])
    def parseE2_(self):
        return self.parseEx_(self.e2_names, self.e2_skips, self.parseE3)

    e4_names = set(['^'])
    e4_skips = set(['*', '/', '//', '%', '$', '+', '-', ')', '|', ','])
    def parseE4_(self):
        #return self.parseEx_(self.e4_names, self.e4_skips, self.parseE5)
        if self.cur.name == '^':
            self.next()
            #lhs = self.parseE5()
            lhs = self.parseE3()
            lst = self.parseE4_()
            return ['^', lhs] + lst
        else:
            return []

    bang = set(['!'])
    e5names = set(['^', '$', '*', '/', '//', '%', '+', '-', ')', '|', ','])
    def parseE5_(self):
        if self.lxin(self.bang):
            self.next()
            if self.parseE5_() is None:
                return '!'
            else:
                return None
        else:
            return None

class Code(object):
    # semi-private. you should probably not build these by-hand.
    def __init__(self, f, names):
        "Construct a Code instance from function 'f' and a list 'names'."
        self.f = f
        self.names = names

    # public
    def run(self, kw):
        "Run the given Code instance using the dictionary 'kw'."
        return self.f(kw)

    # semi-private. requires knowledge of the AST structure.
    @classmethod
    def gen(cls, e):
        "Generate a Code instance given a parse tree 'e'."
        if e.op == 'num':
            if '.' in e.args[0]:
                n = float(e.args[0])
            else:
                n = int(e.args[0])
            return cls(lambda kw: n, [])
        elif e.op == 'id':
            s = e.args[0]
            if s == 'e':
                return cls(lambda kw: math.e, [])
            elif s == 'pi':
                return cls(lambda kw: math.pi, [])
            elif s == 'i':
                return cls(lambda kw: 1j, [])
            else:
                return cls(lambda kw: kw[s], [s])
        elif e.op == '+':
            lhs = Code.gen(e.args[0])
            rhs = Code.gen(e.args[1])
            names = lhs.names + rhs.names
            return cls(lambda kw: lhs.run(kw) + rhs.run(kw), names)
        elif e.op == '-':
            lhs = Code.gen(e.args[0])
            if len(e.args) == 1:
                return cls(lambda kw: -lhs.run(kw), lhs.names)
            else:
                rhs = Code.gen(e.args[1])
                names = lhs.names + rhs.names
                return cls(lambda kw: lhs.run(kw) - rhs.run(kw), names)
        elif e.op == '*':
            lhs = Code.gen(e.args[0])
            rhs = Code.gen(e.args[1])
            names = lhs.names + rhs.names
            return cls(lambda kw: lhs.run(kw) * rhs.run(kw), names)
        elif e.op == '/':
            lhs = Code.gen(e.args[0])
            rhs = Code.gen(e.args[1])
            names = lhs.names + rhs.names
            return cls(lambda kw: float(lhs.run(kw)) / rhs.run(kw), names)
        elif e.op == '%':
            lhs = Code.gen(e.args[0])
            rhs = Code.gen(e.args[1])
            names = lhs.names + rhs.names
            return cls(lambda kw: lhs.run(kw) % rhs.run(kw), names)
        elif e.op == '//':
            lhs = Code.gen(e.args[0])
            rhs = Code.gen(e.args[1])
            names = lhs.names + rhs.names
            return cls(lambda kw: lhs.run(kw) // rhs.run(kw), names)
        elif e.op == '^':
            lhs = Code.gen(e.args[0])
            rhs = Code.gen(e.args[1])
            names = lhs.names + rhs.names
            return cls(lambda kw: lhs.run(kw) ** rhs.run(kw), names)
        elif e.op == '!':
            lhs = Code.gen(e.args[0])
            return cls(lambda kw: math.factorial(lhs.run(kw)), lhs.names)
        elif e.op == 'abs':
            lhs = Code.gen(e.args[0])
            return cls(lambda kw: abs(lhs.run(kw)), lhs.names)
        elif e.op == 'apply':
            fn = e.args[0]
            if fn == 'abs':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: abs(lhs.run(kw)), lhs.names)
            elif fn == 'ceil':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.ceil(lhs.run(kw)), lhs.names)
            elif fn == 'cos':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.cos(lhs.run(kw)), lhs.names)
            elif fn == 'degrees':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.degrees(lhs.run(kw)), lhs.names)
            elif fn == 'floor':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.floor(lhs.run(kw)), lhs.names)
            elif fn == 'log':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.log(lhs.run(kw)), lhs.names)
            elif fn == 'log10':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.log10(lhs.run(kw)), lhs.names)
            elif fn == 'log2':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.log(lhs.run(kw), 2), lhs.names)
            elif fn == 'max':
                args = [Code.gen(arg) for arg in e.args[1:]]
                names = []
                for arg in args: names.extend(arg.names)
                return cls(lambda kw: min([a.run(kw) for a in args]), names)
            elif fn == 'min':
                args = [Code.gen(arg) for arg in e.args[1:]]
                names = []
                for arg in args: names.extend(arg.names)
                return cls(lambda kw: min([a.run(kw) for a in args]), names)
            elif fn == 'radians':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.radians(lhs.run(kw)), lhs.names)
            elif fn == 'round':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: round(lhs.run(kw)), lhs.names)
            elif fn == 'sin':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.sin(lhs.run(kw)), lhs.names)
            elif fn == 'tan':
                lhs = Code.gen(e.args[1])
                return cls(lambda kw: math.tan(lhs.run(kw)), lhs.names)
            else:
                raise Exception("function %r is not defined" % e.args[0])
        else:
            raise Exception("can't handle %r" % e)

# just for playing around or building a REPL. nothing to see here...
class Main(object):
    def tplize(self, s):
        k, v = s.split('=')
        if '.' in v:
            return (k, float(v))
        else:
            return (k, int(v))

    def argdict(self):
        return dict([self.tplize(arg) for arg in sys.argv[2:]])
    
    def gen(self, s):
        return Code.gen(Parser(s).parse())
    
    def execute(self, s, d):
        return self.gen(s).run(d)
    
    def bench(self, s, d, r):
        print s, d, r
        n = 10000
    
        t0 = time.time()
        x = 0
        for i in xrange(0, n):
            x += len(Lexer(s).lex())
        t1 = time.time()
        print "lexed: %s ms" % (t1 - t0)
    
        e = Parser(s).parse()
        t0 = time.time()
        for i in xrange(0, n):
            c = Code.gen(e)
        t1 = time.time()
        print "code-gen: %s ms" % (t1 - t0)
    
        t0 = time.time()
        c = self.gen(s)
        for i in xrange(0, n):
            assert(c.run(d) == r)
        t1 = time.time()
        print "execution only: %s ms" % (t1 - t0)
    
        t0 = time.time()
        for i in xrange(0, n):
            assert(self.execute(s, d) == r)
        t1 = time.time()
        print "full run: %s ms" % (t1 - t0)
    
        print
    
    def cmdrun(self):
        s = sys.argv[1]
        print "input: %s" % s
        d = self.argdict()
    
        e = Parser(s).parse()
        print "lisp: %s" % e.lisp()
    
        c = Code.gen(e)
        if c.names:
            print "variables used: %s" % ', '.join(c.names)
        else:
            print "no variables"
    
        try:
            r = c.run(d)
            print "result: %r" % r
        except KeyError, k:
            print "missing variable: %r" % k.message

    def main(self):
        mode = 'run'

        if mode == 'debug':
            self.cmdrun()

        elif mode == 'bench':
            self.bench("1", {}, 1)
            self.bench("1 + 1", {}, 2)
            self.bench("1 + x", {'x': 9}, 10)
            self.bench("1 + x * 2 + 999", {'x': 3}, 1006)
            self.bench("1 + x * 2 + 999 / y", {'x': 1, 'y': 3}, 336)
            self.bench("log2(2 ^ n * x)", {'n': 8, 'x': 0.5}, 7)
            self.bench("(60 * mapLevel + 3 * mapLevel^2) / 500", {'mapLevel': 1}, 63.0 / 500)

        else:
            print run(sys.argv[1], self.argdict())

if __name__ == "__main__":
    Main().main()

# Calculator Grammar:
#
# non-terminal productions
#   P   -> E1
#   E1  -> E2 E1_
#   E1_ -> + E2 E1_ | - E2 E1_ | e
#   E2  -> E3 E2_
#   E2_ -> * E3 E2_ | / E3 E2_ | // E3 E2_ | % E3 E2_ | e
#   E3  -> E4 | - E4
#   E4  -> E5 E4_
#   E4_ -> ^ E5 E4_ | e
#   E5  -> E6 E5_
#   E5_ -> ! E5_ | e
#   E6  -> num | id A | ( E1 ) | bar E1 bar
#   A   -> ( L ) | e
#   L   -> E1 L_
#   L_  -> , E1 L_ | e
# 
# terminal definitions
#   bar = "|"
#   id  = [a-zA-Z][a-zA-Z0-9]*
#   num = (0|[1-9][0-9]*)(\.[0-9]+)?
#   (plus other literal characters, e.g. +)
# 
# first sets
#   Fi(A)   = ( e
#   Fi(E6)  = num id ( bar
#   Fi(E5_) = ! e
#   Fi(E5)  = Fi(E6)       = num id ( bar
#   Fi(E4_) = ^ e
#   Fi(E4)  = Fi(E5)       = num id ( bar
#   Fi(E3)  = Fi(E4) -     = num id ( bar -
#   Fi(E2_) = * / // % e
#   Fi(E2)  = Fi(E3)       = num id ( bar -
#   Fi(E1_) = + - e
#   Fi(E1)  = Fi(E2)       = num id ( bar -
#   Fi(P)   = Fi(E1)       = num id ( bar -
#   Fi(L)   = Fi(E1)       = num id ( bar -
#   Fi(L_)  = , e
# 
# follow sets
#   Fo(E1)  = ) bar Fi(L_) Fo(L) = ) bar , e
#   Fo(E1_) = Fo(E1)             = ) bar , e
#   Fo(E2)  = Fi(E1_) Fo(E1)     = + - e ) bar ,
#   Fo(E2_) = Fo(E2)             = + - e ) bar ,
#   Fo(E3)  = Fi(E2_) Fo(E2)     = * / // % e + - ) bar ,
#   Fo(E4)  = Fo(E3)             = * / // % e + - ) bar ,
#   Fo(E4_) = Fo(E4)             = * / // % e + - ) bar ,
#   Fo(E5)  = Fi(E4_) Fo(E4)     = ^ e * / // % + - ) bar ,
#   Fo(E5_) = Fo(E5)             = ^ e * / // % + - ) bar ,
#   Fo(E6)  = Fi(E5_) Fo(E5)     = ! e ^ * / // % + - ) bar ,
#   Fo(A)   = Fo(E6)             = ! e ^ * / // % + - ) bar ,
#   Fo(L)   = )
#   Fo(L_)  = Fo(L)              = )
# 
# parse table (non-terminal, list of terminals = production)
#   P    num id ( bar -             = E1
#   E1   num id ( bar -             = E2 E1_
#   E1_  + -                        = [c] E2 E1_
#   E1_  ) bar , $                  = e
#   E2   num id ( bar -             = E3 E2_
#   E2_  * / // %                   = [c] E3 E2_
#   E2_  + - $ ) bar ,              = e
#   E3   -                          = - E3
#   E3   num id ( bar               = E4
#   E4   num id ( bar               = E5 E4_
#   E4_  ^                          = ^ E5 E4_
#   E4_  * / // % $ + - ) bar ,     = e
#   E5   num id ( bar               = E6 E5_
#   E5_  !                          = ! E5_
#   E5_  ^ $ * / // % + - ) bar ,   = e
#   E6   num                        = num
#   E6   id                         = id A
#   E6   (                          = ( E1 )
#   E6   bar                        = bar E1 bar
#   A    (                          = ( L )
#   A    ! e ^ * / // % + - ) bar , = e
#   L    num id ( bar -             = E1 L_
#   L_   ,                          = , E1 L_
#   L_   )                          = e