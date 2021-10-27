using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR6
{
    public class MyAttribute : System.Attribute
    {
        public string Role { get; set; }

        public MyAttribute(string role)
        {
            Role = role;
        }
    }
}
