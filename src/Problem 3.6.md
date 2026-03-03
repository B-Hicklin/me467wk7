A.
In an nxn grid, you need (n^2)^2 propositional sentences for adjacency relations, n x n sentences for creaking rules, and n x n sentences for safety rules (and then another n x n lines for rumbling). In total, you need n^4 + 3(n x n) = n^4 + 3n^2 total sentences. Should n = 100, these means writing a total of 3(100^2) = 100,030,000 sentences.

B.
To encode the warehouse physics in first order logic, only the three following sentences are required:
    {FOR ALL}L Creaking(L) <=> {THERE EXISTS}L' Adjacent(L,L'){NOT}Damaged(L')
    {FOR ALL}L Rumbling(L) <=> {THERE EXISTS}L' Adjacent(L,L'){NOT}Damaged(L')
    {FOR ALL}L Safe(L) <=> {NOT}Damaged(L){AND}{NOT}Forklift(L)
These three lines remain constant for any grid size, a major improvement compared to propositional logic.

C.
In first order logic, the same statement would be written as:
    {THERE EXISTS}L Damaged(L) {AND} {FOR ALL}L' (Damaged(L') => L' = L)
To write the same statement in propositional logic, first write "There is at least one damaged floor tile in the entire warehouse" as:
    D(1,1) {OR} D(1,2) {OR} D(1,3) {OR} ... 
Then, write:
    {Not}D(i,j) {OR} {NOT}D(i',j')
For each individual pair. This totals to ((n^2)*(n^2-1))/2 exclusionary clauses. Don't do this. FOL only every needs the only line.

D.
1:  No. Propositonal encoding quite literally scales exponentially. It would take far too much time to accurately write each and every line. At full 100x100 scale, the propositional logic would need 4(100^2) = 40000 lines to encode the Creaking, Rumbling, Safe, and Adjacent tags, if not more.
2:  For tractable inference, FOL is typically restricted to the following:
    Horn Clauses
    Function-Free FOL
    Description Logics
    Bounded-Variable Fragments
3:  As far as I understand, FOL is already a hybrid system, as the FOL knowledgebase writes propositional logic as it expands and dicovers. This safes the logic engine from having to handle propositional sentences for every single tile, instead only dealing with the relevant ones. These propositonionalized sentences are then used in either forward or backward chaining to determine conclusions.