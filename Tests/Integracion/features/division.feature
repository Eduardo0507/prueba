Feature: Dividir números

    Scenario Outline: División
        Given que deseo dividir dos números
        When yo ingrese los números <num1> y <num2>
        Then El resultado <result> debe ser la división de ambos
        
        Examples: Division de Numeros
        |num1|num2|result|
        |2   |2   |1     |
        |24   |12  |2    |
        |40   |5  |8     |
        |0   |0   |0     |
        |1   |-1  |Invalid|