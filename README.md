Продолжить работу с семинара.
рассмотрим четвертый принцип SOLID - Принцип сегрегации интерфейса (Interface Segregation Principle, ISP). Он гласит: "Клиенты не должны зависеть от интерфейсов, которые они не используют".
Вам надо написать код который исправяет эту ошибку и реализует этот принцип
Пример кода, который нарушает ISP:


public interface Worker {
void work();
void eat();
}

public class HumanWorker implements Worker {
public void work() {
System.out.println("Человек работает");
}

public void eat() {
    System.out.println("Человек ест");
}
}

public class RobotWorker implements Worker {
public void work() {
System.out.println("Робот работает");
}

public void eat() {
    throw new UnsupportedOperationException("Роботы не едят!");
}
}

public class Main {
public static void main(String[] args) {
Worker worker = new RobotWorker();
worker.work();
worker.eat(); // Здесь возникнет исключение UnsupportedOperationException
}
}
В этом примере класс RobotWorker не использует и не должен использовать метод eat(), поэтому он нарушает принцип сегрегации интерфейса.

И аналогично 5-ый принцип

Принцип инверсии зависимостей (Dependency Inversion Principle, DIP) гласит: "Зависимости на абстракциях. Нет зависимостей на что-то конкретное". Это означает, что высокоуровневые модули, которые обеспечивают сложную логику, должны быть независимы от низкоуровневых модулей, которые обеспечивают утилитарные функции. Оба типа модулей должны зависеть от абстракций.

Пример кода, который нарушает DIP:


public class Text {
    String text;

    public Text(String text) {
        this.text = text;
    }

    public String getText() {
        return text;
    }
}

public class Printer {
    public void print(Text text) {
        System.out.println(text.getText());
    }
}

public class Main {
    public static void main(String[] args) {
        Text myText = new Text("Hello, world!");
        Printer myPrinter = new Printer();
        myPrinter.print(myText);
    }
}
В этом примере класс Printer зависит от конкретного класса Text.
