Console.WriteLine("");
Console.WriteLine("Задача 64: Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1.");
int n64 = InputNumbers64("Введите n: ");
int count64 = 2;
PrintNumber64(n64, count64);
Console.Write(1);

void PrintNumber64(int n, int count)
{
    if (count > n) return;
    PrintNumber64(n, count + 1);
    Console.Write(count + ", ");
}

int InputNumbers64(string input)
{
    Console.Write(input);
    int output = Convert.ToInt32(Console.ReadLine());
    return output;
}

Console.WriteLine("");
Console.WriteLine("Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N");
int m66 = InputNumbers66("Введите m: ");
int n66 = InputNumbers66("Введите n: ");
int temp66 = m66;

if (m66 > n66)
{
    m66 = n66;
    n66 = temp66;
}

PrintSumm66(m66, n66, temp66 = 0);

void PrintSumm66(int m, int n, int summ)
{
    summ = summ + n;
    if (n <= m)
    {
        Console.Write($"Сумма элементов= {summ} ");
        return;
    }
    PrintSumm66(m, n - 1, summ);
}

int InputNumbers66(string input)
{
    Console.Write(input);
    int output = Convert.ToInt32(Console.ReadLine());
    return output;
}

Console.WriteLine("");
Console.WriteLine("Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.");
int m68 = InputNumbers68("Введите m: ");
int n68 = InputNumbers68("Введите n: ");

int functionAkkerman68 = Ack68(m68, n68);

Console.Write($"Функция Аккермана = {functionAkkerman68} ");

int Ack68(int m, int n)
{
    if (m == 0) return n + 1;
    else if (n == 0) return Ack68(m - 1, 1);
    else return Ack68(m - 1, Ack68(m, n - 1));
}

int InputNumbers68(string input)
{
    Console.Write(input);
    int output = Convert.ToInt32(Console.ReadLine());
    return output;
}

Console.ReadKey();