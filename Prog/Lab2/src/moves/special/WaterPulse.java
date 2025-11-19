package moves.special;

import ru.ifmo.se.pokemon.*;

public final class WaterPulse extends SpecialMove {
    public WaterPulse() {
        super(Type.WATER, 60, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        if (Math.random() < 0.2) {
            pokemon.confuse();
        }
    }

    @Override
    public String describe() {
        return "использует Water Pulse";
    }
}
