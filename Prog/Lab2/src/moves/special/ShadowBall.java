package moves.special;

import ru.ifmo.se.pokemon.*;

public final class ShadowBall extends SpecialMove {
    public ShadowBall() {
        super(Type.GHOST, 80, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect effect = new Effect().chance(0.2).stat(Stat.SPECIAL_DEFENSE, -1).turns(1);
        pokemon.addEffect(effect);
    }

    @Override
    public String describe() {
        return "использует Shadow Ball";
    }
}
