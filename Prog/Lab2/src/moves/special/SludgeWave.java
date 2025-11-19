package moves.special;

import ru.ifmo.se.pokemon.*;

public final class SludgeWave extends SpecialMove {
    public SludgeWave() {
        super(Type.POISON, 95, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect effect = new Effect().chance(0.1).condition(Status.POISON).turns(1);
        pokemon.addEffect(effect);
    }

    @Override
    public String describe() {
        return "использует Sludge Wave";
    }
}
