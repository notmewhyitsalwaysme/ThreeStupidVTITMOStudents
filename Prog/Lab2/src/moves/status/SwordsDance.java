package moves.status;

import ru.ifmo.se.pokemon.*;

public final class SwordsDance extends StatusMove {
    public SwordsDance() { super(Type.NORMAL, 0, 100); }

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        Effect effect = new Effect().stat(Stat.ATTACK, 2).turns(1);
        pokemon.addEffect(effect);
    }

    @Override
    public String describe() {
        return "использует Swords Dance";
    }
}
