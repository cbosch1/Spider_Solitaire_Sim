# Spider_Solitaire_Sim
A spider solitaire simulator that will be able to run tests on "Rules", telling you which rules to abide by while playing to ensure most
likely victory.

So far the Simulator portion and acompanying tests are complete. While it doesn't print to console, or have any UI,
all that is contained in the Spider_Sim.py file can be used as a backend to create a fully playable single suit Spider Solitaire program. 

Next steps are:

Finish implimentations in Spider_Sim.py that allows for cross suit moves.

Impliment main method in Spider_Sim.py that "runs" a spider solitare game.

Create Spider_Rules.py which will contain statistical tests to run against the Spider_Sim.py program, logging info to
infer best "rules" to play by (I.E. only stack opposites if you can then move a matching card).
