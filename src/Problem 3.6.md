A.
In an nxn grid, you need n x n propositional sentences for adjacency relations, n x n sentences for creaking rules, and nxn sentences for safety rules. In total for theese three rule types, you need 3(n x n) = 3n^2 total sentences. Should n = 100, these means writing a total of 3(100^2) = 30,000 sentences.

B.
In first order logic, the following sentences are required:
    Adjacent_fn = Function('Adjacent', Location, Location, BoolSort())
    for x in range(1, width + 1):
        for y in range(1, height + 1):
            adj_set = set(get_adjacent(x, y, width, height))
            for x2 in range(1, width + 1):
                for y2 in range(1, height + 1):
                    if (x2, y2) in adj_set:
                        solver.add(Adjacent_fn(loc[(x, y)], loc[(x2, y2)]))
                    else:
                        solver.add(Not(Adjacent_fn(loc[(x, y)], loc[(x2, y2)])))
    Creaking_fn = Function('Creaking', Location, BoolSort())
    Safe_fn = Function('Safe', Location, BoolSort()) 
     solver.add(ForAll(L,
        Creaking_fn(L) == Exists(Lp, And(Adjacent_fn(L, Lp), Damaged_fn(Lp)))
    ))
    solver.add(ForAll(L,
        Safe_fn(L) == And(Not(Damaged_fn(L)), Not(Forklift_fn(L)))
    ))
At only eighteen lines, this is an improvement over even a 3x3 grid, which needs 3(3^2) = 27.    

C.
To my knowledge, the statement "There is exactly one damaged floor tile in the entire warehouse" cannot be written in propositional logic. However, you can write "There is at least one damaged floor tile in the entire warehouse", or simply define one and only one tile as being damaged in the environment setup. In first order logic, the same statement would be written as:
    {backwards capital E}!location Damaged(location)

D.
1:  No. Propositonal encoding quite literally scales exponentially. It would take far too much time to accurately write each and every line. At full 100x100 scale, the propositional logic would need 4(100^2) = 40000 lines to encode the Creaking, Rumbling, Safe, and Adjacent tags, if not more.
2:  For tractable inference, FOL is typically restricted to Definite Clauses, Datalogs, and/or Description logics.
3:  As far as I understand, FOL is already a hybrid system, as the FOL knowledgebase writes propositional logic as it expands and dicovers. This safes the logic engine from having to handle propositional sentences for every single tile, instead only dealing with the relevant ones. These propositonionalized sentences are then used in either forward or backward chaining to determine conclusions.