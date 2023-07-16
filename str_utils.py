def strInBox(msg: str, boxlen: int, boxchar="#"):
    """Print message msg in a box of a certain character. This box has lenghts boxlen.
        if boxlen is to short to wrap the message, boxlen is automatically corrected upwards
    Args:
        msg (str): message to print
        boxlen (int): length of the box
        boxchar (str, optional): character to use as box marker. Defaults to "#".

    Returns:
        str: Example: msg="msg", boxlen = 7, boxchar="?"
            -> "???????
                ? msg ?
                ???????"
    """
    # message too long for given boxlen? -> extend boxlen
    least_possible_boxlen = len(msg) + 2
    if boxlen < least_possible_boxlen:
        boxlen = least_possible_boxlen
    fence = boxlen * boxchar
    num_chars_to_fill = boxlen - 2 - len(msg)
    num_chars_to_fill_oneside = int(num_chars_to_fill / 2)
    fillspace = num_chars_to_fill_oneside * " "
    res = fence + "\n"
    res += boxchar + fillspace + msg + fillspace + boxchar + "\n" + fence
    return res
