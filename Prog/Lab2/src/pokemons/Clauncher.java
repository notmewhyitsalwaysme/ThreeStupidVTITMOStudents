package pokemons;

import ru.ifmo.se.pokemon.*;
import moves.special.*;

public class Clauncher extends Pokemon {
    public Clauncher(String name, int level) {
        super(name, level);
        setType(Type.WATER);
        setStats(50, 53, 62, 58, 63, 44);
        setMove(new Venoshock(), new SludgeWave(), new WaterPulse());
    }
}