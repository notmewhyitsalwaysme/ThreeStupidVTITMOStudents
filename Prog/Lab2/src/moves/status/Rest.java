package moves.status;

import ru.ifmo.se.pokemon.*;

public final class Rest extends StatusMove {
    public Rest() {
        super(Type.PSYCHIC, 0, 100);
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        double maxHP = pokemon.getStat(Stat.HP);
        double currentHP = pokemon.getHP();
        Effect effect = new Effect().condition(Status.SLEEP).stat(Stat.HP, -1 * (int) (maxHP - currentHP)).turns(2);
        pokemon.addEffect(effect);
    }

    @Override
    public String describe() {
        return "использует Rest";
    }
}
