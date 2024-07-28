import shutil


def ft_tqdm(lst: range) -> None:
    """
    Simulate a progress bar for iterating through a range.

    Args:
        lst (range): The range to iterate through.

    Yields:
        Any: The current item from the range.
        is a keyword in Python used in the context of creating generators.
        Generators are a way to create iterators, which are objects used to
        iterate over a sequence of values without having to store all those
        values in memory at once. Instead of generating allvalues and returning
        them in one go, a generator yields one value at a time whenever the
        yield statement is encountered.
    """
    total = len(lst)
    terminal_width = shutil.get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10
    # enumerate parcour lst tout en gardant
    # une trace de l'index de chaque élément
    for i, val in enumerate(lst, start=1):

        # val represente l'element actuel de lst
        # yield val sert à retourner l'élément de lst sans terminer la fonction
        # elle renvoie un résultat au générateur appelant
        # et conserve l'état de la fonction pour que l'exécution
        # puisse reprendre là où elle s'est arrêtée lors du prochain appel
        yield val

        # proportion de la barre parcourue
        # converti en int si on obtient un float
        progress = int(i / total * progress_bar_width)

        # {'█' * progress:<{progress_bar_width}} signifie qu'on veut
        # aligné le █ à gauche dans le champ de largeur progress_bar_width
        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        # affiche la progression de la barre formatté comme dans le sujet
        # '\r' permet de overwrite la ligne recente de la progression
        print(f"{progress_info}", end="\r", flush=True)
