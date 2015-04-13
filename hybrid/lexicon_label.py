def prune():
    from glob import glob

    MAIN_PATH = "../data/aclImdb/test"
    POS_PATH = MAIN_PATH + "/pos"
    NEG_PATH = MAIN_PATH + "/neg"

    len_files = {}
    for path in [POS_PATH, NEG_PATH]:
        label = path[-3:]
        print "Compiling file list... (%s)" % label
        files = glob(path+"/[!.]*.txt")
        len_files[label] = len(files)

        print "Pruning files... (%s)" % label
        for file in files:
            with open(file, 'r') as f:
                data.append(f.read())

        targets += [target_names.index(label)]*len_files[label]

    print "Done."

    return (data, targets, target_names)
