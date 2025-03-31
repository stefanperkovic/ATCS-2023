def print_sum(in_path):

    sum = 0
    with open(in_path, "r") as file:
        line = file.readline()
        while line:
            try:
                sum += int(line)
            except ValueError:
                print(line)
            line = file.readline()      
    print(sum)


def calculate_costs(purchase_path, cost_path, out_path):

    costs_dic = {}
    with open(cost_path, "r") as file:
        line = file.readline()
        while line:
            lst_cost = line.split()
            costs_dic[lst_cost[0]] = lst_cost[1]
            line = file.readline()

    total_spend = {}
    with open(purchase_path, "r") as file:
        line = file.readline()
        while line:
            purchases_lst = line.split()
            sum = 0
            for i in range(1, len(purchases_lst)):
                sum += costs_dic[purchases_lst[i]]
            total_spend[purchases_lst[0]] = sum

            line = file.readline()
    
    with open(out_path, "w") as file:
        for key, value in total_spend:
            file.write(key + ": " + value)


def rna_to_aa(rna_path, aa_path, out_path):

    rna = ""
    with open(rna_path, "r") as file:
        line = file.readline()
        start = line.index("AUG")
        end = line.index("UAG")
        rna_string = line[start: end + 1]

        for i in range(0, len(rna_string), 3):      
            with open(aa_path, "r") as file:
                line = file.readline()
                while line:
                    amino_acid_pairs = line.split()
                    for j in range(1, len(amino_acid_pairs)):
                        if (rna_string[i : i+3] == amino_acid_pairs[j]):
                            rna += amino_acid_pairs[0]

    with open(out_path, "w") as file:
        file.write(rna)

    

    







