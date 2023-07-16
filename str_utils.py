def strInBox(msg: str, boxlen: int, boxchar="#"):
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
