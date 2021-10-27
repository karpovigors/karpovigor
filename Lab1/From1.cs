
            if (y2 > 0)
            {
                Console.ForegroundColor = ConsoleColor.Green; // устанавливаем цвет
                x3 = -Math.Sqrt(y2);
                x4 = Math.Sqrt(y2);
                Console.WriteLine("x3={0}, x4={1}", x3, x4);
                Console.ResetColor(); // сбрасываем в стандартный
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red; // устанавливаем цвет
                x3 = -Math.Sqrt(y2);
                x4 = Math.Sqrt(y2);
                Console.WriteLine("x3={0}, x4={1}", x3, x4);
                Console.ResetColor(); // сбрасываем в стандартный
            }
        }
    }
}


