using System;

namespace Lab2
{
    interface IPrint
    {
        void Print()
        {
        }
    }
    abstract class Geometric_figure // "Геометрическая фигура"
    {
        public double area;
        public virtual double Area_calculation(double length, double width)
        {
            area = width * length;
            return area;
        }
        public virtual double Area_calculation(double radius)
        {
            area = Math.PI * (radius * radius);
            return area;
        }


    }
    class Rectangle : Geometric_figure, IPrint // "Прямоугольник"
    {
        public double height;
        public double width;


 
        public Rectangle(double h, double w) 
        {
            height = h;
            width = w;
            Area_calculation(h, w);
        }
        public override string ToString()
        {
            return String.Concat("Прямоугольник - Длина: ", height, " Ширина: ", width, " Площадь: ", area);
        }
  

        public Rectangle()
        {
            height = 0;
            width = 0;
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
    class Square : Rectangle, IPrint
    {
        public double storon;
        public Square(double s) : base(s,s)
        {
            storon=s;
            Area_calculation(s, s);
        }
        public override string ToString()

        {
            return String.Concat("Квадрат - Длина: ", storon, " Площадь: ", area);
        }
        public new void Print()
        {
            Console.WriteLine(ToString());
        }
    }

    class Circle : Geometric_figure, IPrint
    {
        public double radius;
        public Circle(double r)
        {
            radius=r;
            Area_calculation(r);
        }
        public override string ToString()

        {
            return String.Concat("Круг - Радиус: ", radius, " Площадь: ", area);
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }

    }
   
    class Program
    {
        static void PrintV(IPrint pr)
        {
            pr.Print();
        }
        static void Main(string[] args)
        {
            Rectangle obj1=new Rectangle(5,6);
            PrintV(obj1);

            Square obj2 = new Square(5);
            PrintV(obj2);

            Circle obj3 = new Circle(4);
            PrintV(obj3);

        }
    }
}








