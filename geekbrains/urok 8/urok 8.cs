Console.WriteLine("Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.");
int[,] table54 = new int[3, 4];
FillArrayRandom54(table54);
PrintArray54(table54);
SortToLower54(table54);
Console.WriteLine();
PrintArray54(table54);



void FillArrayRandom54(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = new Random().Next(1, 10);
        }
    }
}

void SortToLower54(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(1) - 1; k++)
            {
                if (array[i, k] < array[i, k + 1])
                {
                    int temp = array[i, k + 1];
                    array[i, k + 1] = array[i, k];
                    array[i, k] = temp;
                }
            }
        }
    }
}

void PrintArray54(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write($"{array[i, j]} ");
        }
        Console.WriteLine();
    }
}


Console.WriteLine("Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.");
Console.WriteLine("Введите размер массива m x n и диапазон случайных значений:");
int m56 = InputNumbers56("Введите m: ");
int n56 = InputNumbers56("Введите n: ");
int range56 = InputNumbers56("Введите диапазон: от 1 до ");

int[,] array56 = new int[m56, n56];
CreateArray56(array56);
WriteArray56(array56);

int minSumLine56 = 0;
int sumLine56 = SumLineElements56(array56, 0);
for (int i56 = 1; i56 < array56.GetLength(0); i56++)
{
    int tempSumLine = SumLineElements56(array56, i56);
    if (sumLine56 > tempSumLine)
    {
        sumLine56 = tempSumLine;
        minSumLine56 = i56;
    }
}

Console.WriteLine($"\n{minSumLine56 + 1} - строкa с наименьшей суммой ({sumLine56}) элементов ");


int SumLineElements56(int[,] array, int i)
{
    int sumLine = array[i, 0];
    for (int j = 1; j < array.GetLength(1); j++)
    {
        sumLine += array[i, j];
    }
    return sumLine;
}

int InputNumbers56(string input)
{
    Console.Write(input);
    int output = Convert.ToInt32(Console.ReadLine());
    return output;
}

void CreateArray56(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = new Random().Next(range56);
        }
    }
}

void WriteArray56(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}



Console.WriteLine("Задача 58: Напишите программу, которая заполнит спирально массив 4 на 4. \n");
int n58 = 4;
int[,] sqareMatrix58 = new int[n58, n58];

int temp58 = 1;
int i58 = 0;
int j58 = 0;

while (temp58 <= sqareMatrix58.GetLength(0) * sqareMatrix58.GetLength(1))
{
    sqareMatrix58[i58, j58] = temp58;
    temp58++;
    if (i58 <= j58 + 1 && i58 + j58 < sqareMatrix58.GetLength(1) - 1)
        j58++;
    else if (i58 < j58 && i58 + j58 >= sqareMatrix58.GetLength(0) - 1)
        i58++;
    else if (i58 >= j58 && i58 + j58 > sqareMatrix58.GetLength(1) - 1)
        j58--;
    else
        i58--;
}

WriteArray58(sqareMatrix58);

void WriteArray58(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (array[i, j] / 10 <= 0)
                Console.Write($" {array[i, j]} ");

            else Console.Write($"{array[i, j]} ");
        }
        Console.WriteLine();
    }
}



Console.ReadKey();