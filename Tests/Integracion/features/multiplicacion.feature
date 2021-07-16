Feature: Multiplicar números

    Scenario Outline: Multiplicación
        Given que deseo multiplicar dos números
        When yo ingrese los números <num1> y <num2>
        Then El resultado <result> debe ser la multiplicación de ambos
        
        Examples: Multiplicacion de Numeros
        |num1|num2|result|
        |2   |2   |4     |
        |1   |12  |12    |
        |10 |50 |500  |
        |0   |0   |0     |
        |1   |-1  |Invalid|