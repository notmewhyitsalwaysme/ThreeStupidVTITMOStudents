package moves.physical;

import ru.ifmo.se.pokemon.*;

public final class Facade extends PhysicalMove{
    public Facade() {
        super(Type.NORMAL, 70, 100);
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        Status condition = pokemon.getCondition();
        if (condition == Status.BURN || condition == Status.POISON || condition == Status.PARALYZE) {
            Effect effect = new Effect().stat(Stat.ATTACK, 2).turns(1);
            pokemon.addEffect(effect);
        }
    }

    @Override
    protected String describe() {
        return "использует Facade";
    }
}
