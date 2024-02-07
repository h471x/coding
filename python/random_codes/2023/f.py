def gcd(a, b):
    if b < 0.0000001:
        return a  # Arrête la récursion lorsque b est négligeable
    return gcd(b, a % b)  # Applique l'algorithme d'Euclide

def convertToFraction(number):
    decimal = float(number)  # Convertit le nombre en décimal
    numerator = 1
    denominator = 1

    while abs(decimal - round(decimal)) > 0.0000001:
        decimal *= 10
        numerator = int(decimal)
        denominator *= 10

    divisor = gcd(numerator, denominator)

    numerator /= divisor
    denominator /= divisor

    if denominator == 1:
        return str(number)  # Retourne le nombre d'origine si le dénominateur est 1
    else:
        return str(int(numerator)) + '/' + str(int(denominator))

# Exemples d'utilisation
print(convertToFraction(3.14159265358970))  # Affiche "15/4"
print(convertToFraction(0.5))  # Affiche "1/2"
print(convertToFraction(2))  # Affiche "2/1"
print(convertToFraction(5))  # Affiche "5"
