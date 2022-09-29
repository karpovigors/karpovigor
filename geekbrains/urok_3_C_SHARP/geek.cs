string hello = "Привет мир";
Console.WriteLine(hello);


Console.WriteLine("Задача 19 Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.");
Console.WriteLine("Введите число: ");
string number = Console.ReadLine();
int len = number.Length;
if (len == 5)
{
    if (number[0] == number[4] && number[1] == number[3])
    {
        Console.WriteLine($"{number} - Палиндром");
    }
    else
    {
        Console.WriteLine($"{number} - НЕ палиндром");
    }
}
else
{
    Console.WriteLine($"ОШИБКА: {number} - не является пятизначным");
}


Console.WriteLine("Задача 21 (branch task_2) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.");
int x1 = ReadInt("Введите координату X первой точки: ");
int y1 = ReadInt("Введите координату Y первой точки: ");
int z1 = ReadInt("Введите координату Z первой точки: ");
int x2 = ReadInt("Введите координату X второй точки: ");
int y2 = ReadInt("Введите координату Y второй точки: ");
int z2 = ReadInt("Введите координату Z второй точки: ");

int A = x2 - x1;
int B = y2 - y1;
int C = z1 - z2;

double length = Math.Sqrt(A * A + B * B + C * C);
Console.WriteLine($"Длинна отрезка {length}");
// Функция ввода сообщения
int ReadInt(string message)
{
    Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}


Console.WriteLine("Задача 23 Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.");
int number1 = ReadInt("Введите число N: ");
for (int i = 1; i <= number1; i++)
{
    Console.Write($"{i * i * i} ");
}
// Функция ввода сообщения
int ReadInt1(string message)
{
    Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

Console.ReadKey();


