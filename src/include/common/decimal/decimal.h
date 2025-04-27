#ifndef DECIMAL_H
#define DECIMAL_H

#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

class Decimal {
public:
    Decimal();

    explicit Decimal(const std::string &value);

    Decimal(const Decimal &other);

    Decimal &operator=(const Decimal &other);

    Decimal operator+(const Decimal &other) const;

    Decimal operator-(const Decimal &other) const;

    Decimal operator*(const Decimal &other) const;

    Decimal operator/(const Decimal &other) const;

    friend std::ostream &operator<<(std::ostream &os, const Decimal &dec);

private:
    std::string value;
};

#endif // DECIMAL_H
