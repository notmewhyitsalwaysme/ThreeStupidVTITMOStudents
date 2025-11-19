package moves.special;

import ru.ifmo.se.pokemon.*;

public final class Venoshock extends SpecialMove {
    public Venoshock() {
        super(Type.POISON, 65, 100);
    }

    @Override
    protected void applyOppDamage(Pokemon pokemon, double damage) {
        Status condition = pokemon.getCondition();
        if (condition == Status.POISON) {
            Effect effect = new Effect().stat(Stat.HP, 2 * (int) damage).turns(1);
            pokemon.addEffect(effect);
        }
    }

    @Override
    public String describe() {
        return "использует Venoshock";
    }
}
