def pb_init(text:str) -> int:
    print(text, end='', flush=True)
    return 0

def pb_update(iter:int, total:int, old_nbars:int, length:int = 40) -> int:
    nbars = int(length * iter // total)
    ten = length // 10
    
    for i in range(old_nbars, nbars):
        imod10 = i % ten
        if (imod10 == 0 and i != 0):
            print(i // ten * 10, end='')
        print('-', end='')

    if iter == total:
        print(100)
    
    print("", end="", flush=True)

    return nbars
    
def print_progress_bar(iteration, total, prefix='', suffix='', usePercentage=False, decimals=1, length=80, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration      - Required  : current iteration (Int)
        total          - Required  : total iterations (Int)
        prefix         - Optional  : prefix string (Str)
        suffix         - Optional  : suffix string (Str)
        decimals       - Optional  : positive number of decimals in percent complete (Int)
        length         - Optional  : character length of bar (Int)
        fill           - Optional  : bar fill character (Str)
        printEnd       - Optional  : end character (e.g. "\r", "\r\n") (Str)
        usePercentage  - Optional  : show percentage instead of 'iteration/total' (Bool)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)

    if usePercentage:
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    else:
        print(f'\r{prefix} |{bar}| {iteration:>{len(f"{total}")}}/{total} {suffix}', end=printEnd)

    # Print New Line on Complete
    if iteration == total:
        print()


def print_progress(iteration, total, prefix='', suffix='', decimals=1, printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    print(f'\r{prefix} {iteration}/{total} ({percent}%) {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

if __name__ == "__main__":
    pass