package moves.status;

import ru.ifmo.se.pokemon.*;

public final class SweetScent extends StatusMove {
    public SweetScent() {
        super(Type.NORMAL, 0, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect effect = new Effect().stat(Stat.EVASION, -1).turns(1);
        pokemon.addEffect(effect);
    }

    @Override
    public String describe() {
        return "использует Sweet Scent";
    }
}
