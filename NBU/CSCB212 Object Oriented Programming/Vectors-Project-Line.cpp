#include "Line.h"
#include"../vector/Vector.h"
#include"../point/Point.h"

using namespace std;

Line::Line(){
    point = Point();
    vector = Vector();
}

Line::Line(Point &x, Vector &a) {
    point = x;
    vector = a;
}

Line::Line(Point &x, Point &y) {
    point = x;
    vector = Vector(x, y);
}

Vector Line::getVector() const{
    Vector new_vector;
    double x = this->vector.getX();
    double y = this->vector.getY();
    double z = this->vector.getZ();

    new_vector = Vector(x, y, z);
    return new_vector;
}

Point Line::getPoint() const{
    Point a;

    double x = this->point.getX();
    double y = this->point.getY();
    double z = this->point.getZ();

    a = Point(x, y, z);
    return a;
}

Vector Line::getDirection() const {

}

Vector Line::getPerpendicular() const {

}

double Line::calculatePointDistance(Point x) const
{
    // https://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html

    Vector new_vector;

    Point current_point = this->getPoint();
    new_vector = Vector(current_point,  x);

    double distance = ((this->getVector() ^ new_vector)->getLength() / this->getVector().getLength());
    return distance;
}

double Line::calculateLineDistance(const Line& x) const{
    Vector a,  b, current_vector, x_vector;

    Point current_point = this->getPoint();
    Point x_point = x.getPoint();

    current_vector = this->getVector();
    x_vector = x.getVector();

    a = Vector(current_point, x_point);
    b  = *(current_vector ^ x_vector);

    if (abs(b.getLength()) < 0.1){
        return abs(this->getVector().getLength());
    }
    else {
        double distance = current_vector * x_vector;
        return abs(distance / b.getLength());
    }
 }

Line& Line::operator=(const Line& x) {
    if (this != &x) {
        this->point = x.point;
        this->vector = x.vector;
    }
    return *this;
}

bool Line::operator+(const Point& x) const {
        return abs(this->calculatePointDistance(x)) < 0.1;
}

bool Line::operator||(const Line&) const {

}

bool Line::operator&&(const Line& c) const {
    if (!(*this || c)) {
        return this->calculateLineDistance(c) < 0.1 && this->calculateLineDistance(c) > -0.1;
    }
    return false;
}

bool Line::operator==(const Line& x) const {
    if (this->getVector().isParallelWith(x.getVector())) {
        return abs(this->calculateLineDistance(x)) < 0.1;
    }
    return false;
}

bool Line::operator|(const Line& x) const{
    Vector a, b;
    a = this->getVector();
    b = x.getVector();

    return abs(a.getX() * b.getX() + a.getY() * b.getY() + a.getZ() * b.getZ()) < 0.1;
 }




Line::~Line() = default;


