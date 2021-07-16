Feature: Restar números

    Scenario Outline: Resta
        Given que deseo restar dos números
        When yo ingrese los números <num1> y <num2>
        Then El resultado <result> debe ser la resta de ambos
        
        Examples: Resta de Numeros
        |num1|num2|result|
        |6   |3   |3    |
        |23  |13  |13    |
        |750  |250   |500   |
        |1   |1   |0    |
        |1  |-1  |Invalid|