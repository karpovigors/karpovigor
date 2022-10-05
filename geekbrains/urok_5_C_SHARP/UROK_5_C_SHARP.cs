string hello = "Привет мир";
Console.WriteLine(hello);
Console.WriteLine("Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.");
Console.WriteLine("Введите размер массива");
int size = Convert.ToInt32(Console.ReadLine());
int[] numbers = new int[size];
int count = 0;
FillArrayRandomNumbers(numbers);
PrintArray(numbers);


for (int i = 0; i < numbers.Length; i++)
{
    if (numbers[i] % 2 == 0)
        count++;
}


Console.WriteLine($"количество чётных чисел в массиве -> {count} ");

void FillArrayRandomNumbers(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(100, 1000);
    }
}
void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}

Console.WriteLine("Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.");
int size1 = 4;
int[] numbers1 = new int[size1];
FillArrayRandomNumbers1(numbers);
PrintArray1(numbers);

int sumNumbersEvenIndex = 0;

for (int i = 1; i < numbers.Length; i += 2)
{
    sumNumbersEvenIndex += numbers[i];
}
Console.Write(sumNumbersEvenIndex);



void FillArrayRandomNumbers1(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(-100, 101);
    }
}

void PrintArray1(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}




Console.WriteLine("Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.");
int size2 = 10;
int[] numbers2 = new int[size2];
FillArrayRandomNumbers2(numbers);
PrintArray2(numbers);

int max = numbers[0];
int min = numbers[0];

for (int i = 0; i < numbers.Length; i++)
{
    if (numbers[i] > max)
    {
        max = numbers[i];
    }
    else if (numbers[i] < min)
    {
        min = numbers[i];
    }
}

Console.WriteLine($"Минимальное число: {min}");
Console.WriteLine($"Минимальное число: {max}");
Console.WriteLine($"Разница между максимальным и минимальным числами: {max - min}");



void FillArrayRandomNumbers2(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(1, 555);
    }
}


void PrintArray2(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}

Console.ReadKey();