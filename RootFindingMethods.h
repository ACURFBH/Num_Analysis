#ifndef ROOTFINDINGMETHODS_H
#define ROOTFINDINGMETHODS_H


class RootFindingMethods
{
    public:
        double getRoot();
        int getIter();
        RootFindingMethods();
        virtual ~RootFindingMethods();
        double bisection(double, double, int);
        double newton(double, int);
    private:
        double root;
        int iter;
        void iterate();
        double bisect_rec(double, double, double);
        double bisect_loop(double, double, double);
};

#endif // ROOTFINDINGMETHODS_H
