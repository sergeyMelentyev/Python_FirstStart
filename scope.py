var = 99                                            # global var


def local():                                        # change local var
    var = 0
    print(var)


def global_one():                                    # change global var
    global var
    var += 1


def global_two():                                    # change global var
    import scope
    scope.var += 1


def global_three():                                  # change global var
    import sys
    glob = sys.modules['scope']
    glob.var += 1
