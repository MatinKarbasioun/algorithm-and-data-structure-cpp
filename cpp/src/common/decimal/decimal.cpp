#include "common/decimal/decimal.h"
#include <stdexcept>


Decimal::Decimal() : value("0") {}

Decimal::Decimal(const std::string &value) : value(value) {}

Decimal::Decimal(const Decimal &other) : value(other.value) {}

Decimal &Decimal::operator=(const Decimal &other) {
    if (this != &other) {
        value = other.value;
    }
    return *this;
}

Decimal Decimal::operator+(const Decimal &other) const {
    // For simplicity, use double for this example
    double result = std::stod(value) + std::stod(other.value);
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(10) << result;
    return Decimal(oss.str());
}

Decimal Decimal::operator-(const Decimal &other) const {
    double result = std::stod(value) - std::stod(other.value);
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(10) << result;
    return Decimal(oss.str());
}

Decimal Decimal::operator*(const Decimal &other) const {
    double result = std::stod(value) * std::stod(other.value);
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(10) << result;
    return Decimal(oss.str());
}

Decimal Decimal::operator/(const Decimal &other) const {
    if (other.value == "0") {
        throw std::invalid_argument("Division by zero");
    }
    double result = std::stod(value) / std::stod(other.value);
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(10) << result;
    return Decimal(oss.str());
}

std::ostream &operator<<(std::ostream &os, const Decimal &dec) {
    os << dec.value;
    return os;
}
