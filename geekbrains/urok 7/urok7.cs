Console.WriteLine("Задача 47: Задайте двумерный массив размером m×n, заполненный случайными вещественными числами, округлёнными до одного знака.");
Console.WriteLine("Задайте количество строк двумерного массива:");
int m47 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Задайте количество столбцов двумерного массива:");
int n47 = Convert.ToInt32(Console.ReadLine());
double[,] twoDimArray = new double[m47, n47];
Random rnd = new Random();
void PrintArray(double[,] matr)
{
    for (int i = 0; i < m47; i++)
    {
        for (int j = 0; j < n47; j++)
        { Console.Write($"{matr[i, j]} "); }
        Console.WriteLine();
    }
}

void FillArray(double[,] matr)
{
    for (int i = 0; i < m47; i++)
    {
        for (int j = 0; j < n47; j++)
        { matr[i, j] = Convert.ToDouble(rnd.Next(-100, 100) / 10.0); }
    }
}
FillArray(twoDimArray);
Console.WriteLine();
PrintArray(twoDimArray);



Console.WriteLine("Задача 50: Напишите программу, которая на вход принимает индексы элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.");
Console.WriteLine("Введите размеры массива");
int m50 = Convert.ToInt32(Console.ReadLine());
int n50 = Convert.ToInt32(Console.ReadLine());
int[,] array = new int[m50, n50];

for (int i = 0; i < array.GetLength(0); i++)
{
    for (int j = 0; j < array.GetLength(1); j++)
        array[i, j] = Convert.ToInt32(new Random().Next(0, 21));
}

for (int i = 0; i < array.GetLength(0); i++)
{
    for (int j = 0; j < array.GetLength(1); j++)
        Console.Write(array[i, j] + "\t  ");
    Console.WriteLine();
}

Console.WriteLine("Введите координаты начиная с число 0");
int a = Convert.ToInt32(Console.ReadLine());
int b = Convert.ToInt32(Console.ReadLine());
if (a > m50 && b > n50)
    Console.WriteLine("Такого числа нет");
else
{
    object c = array.GetValue(a, b);
    Console.WriteLine(c);
}


Console.WriteLine("Задача 52: Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.");
Console.WriteLine("Задайте количество строк двумерного массива:");
int m52 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Задайте количество столбцов двумерного массива:");
int n52 = Convert.ToInt32(Console.ReadLine());
int[,] twoDimArray52 = new int[m52, n52];
Random rnd52 = new Random();
void PrintArray52(int[,] matr)
{
    for (int i = 0; i < m52; i++)
    {
        for (int j = 0; j < n52; j++)
        { Console.Write($"{matr[i, j]} "); }
        Console.WriteLine();
    }
}

void FillArray52(int[,] matr)
{
    for (int i = 0; i < m52; i++)
    {
        for (int j = 0; j < n52; j++)
        { matr[i, j] = Convert.ToInt32(rnd.Next(0, 100) / 10); }
    }
}
void ArithmeticNumber(int[,] matr)
{

    double[] s = new double[n52];
    //сумма по столбцу
    Console.WriteLine("Среднее арифметическое число каждого столбца");
    for (int i = 0; i < n52; i++)
    {
        for (int j = 0; j < m52; j++)
            s[i] += matr[j, i];
        Console.Write($"{s[i]/m52} ");
    }

}
FillArray52(twoDimArray52);
Console.WriteLine();
PrintArray52(twoDimArray52);
ArithmeticNumber(twoDimArray52);



Console.ReadKey();