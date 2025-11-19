import ru.ifmo.se.pokemon.*;
import pokemons.*;

public class Main {
    public static void main(String[] args) {
        Battle battle = new Battle();

        Pokemon p1 = new Furfrou("Железный Вихрь", 1);
        Pokemon p2 = new Clawitzer("Рокот Бездны", 1);
        Pokemon p3 = new Oddish("Шёпот Клинков", 1);

        Pokemon p4 = new Clauncher("Гнев Валькирии", 1);
        Pokemon p5 = new Gloom("Последний Рубеж", 1);
        Pokemon p6 = new Bellossom("Танец Теней", 1);

        battle.addFoe(p1); battle.addFoe(p2); battle.addFoe(p3);
        battle.addAlly(p4); battle.addAlly(p5); battle.addAlly(p6);

        battle.go();
    }
}