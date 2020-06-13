#ifndef LINE
#define LINE

#include"../vector/Vector.h"
#include"../point/Point.h"

class Line : public Vector {
private:
    Point point;
    Vector vector;
public:
    Line();
    Line(Point &, Point &);
    Line(Point &, Vector &);
    ~Line();

    Vector getVector() const;
    Point getPoint() const;
    Vector getDirection() const;
    Vector getPerpendicular() const;
    double getAngle(const Line&) const;

    double calculatePointDistance(Point) const;
    double calculateLineDistance(const Line&) const;


    bool operator+(const Point&) const;
    bool operator||(const Line&) const;
    bool operator==(const Line&) const;
    bool operator&&(const Line&) const;
    bool operator!=(const Line&) const;
    bool operator|(const Line&) const;

    Line& operator=(const Line&);
};

#endif // LINE