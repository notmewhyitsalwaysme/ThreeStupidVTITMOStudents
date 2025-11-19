package moves.status;

import ru.ifmo.se.pokemon.*;

public final class SleepPowder extends StatusMove {
    public SleepPowder() {
        super(Type.GRASS, 0, 75);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect effect = new Effect().condition(Status.SLEEP).turns(1);
        pokemon.setCondition(effect);
    }

    @Override
    public String describe() {
        return "использует Sleep Powder";
    }
}
