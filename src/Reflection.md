(a)
Rule count scales significantly more aggressivly for the propositional approach. In propositional logic, every single tile in the grid needs its own written rules; in FOL, the predicates handle each tile as necessary. This makes the FOL appoarch much more fficient for larger grids.

(b)
Again, it somewhat depends on the grid size. At smaller grids, I'd give it to the propositional, as you can analyse each and every line of its thinking to know what its doing. In FOL, you have to trust the computer to make the correct jugements and records. At large grids, the myriad lines of code necessary for propositional encoding simply become too large to understand.

(c)
Domain encosure tells the FOL engine when to stop. Unlike propositional encoding, FOL is set up to adjust to any grid size by making the grid spaces as it goes. Without any brakes, the system could hallucinate its way into an infinite grid, far exceeding the boundaries of the actual problem. Encosing the domain puts boundaries on the FOL encoding, allowing it to 'color within the lines' without issue. As propositional logic doesn't create grid spaces and instead has every possible grid square defined for it, it doesn't need domain enclosure.