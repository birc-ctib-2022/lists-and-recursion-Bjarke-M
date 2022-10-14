"""Linked lists."""

from __future__ import annotations
from ast import Not
from pickle import FALSE
from re import A
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass
from unittest import result

T = TypeVar('T')


@dataclass
class L(Generic[T]):
    """
    A single link in a linked list.

    The `head` attribute gives you the value at the head of
    this list while `tail` gives you the rest of the list,
    or None if the rest is the empty list.

    >>> L(1, L(2, L(3, None)))
    L(1, L(2, L(3, None)))
    """

    head: T
    tail: List[T]

    def __repr__(self) -> str:
        """Representation of this object."""
        return f"L({self.head}, {self.tail})"


List = Optional[L[T]]  # A list is an L() constructor or None


# Direct recursive versions ###########################################


def length(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length(None)
    0
    >>> length(L(1, None))
    1
    >>> length(L(1, L(2, L(3, None))))
    3
    """
    return 0 if x is None else 1 + length(x.tail)
# as match statement instead 
# match x:
#     case None: return 0
#     case L(_,tail): return 1+length(tail)
# complexity O(n), but as it is both worst and best Theta(n)

def add(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> add(None)
    0
    >>> add(L(1, None))
    1
    >>> add(L(1, L(2, L(3, None))))
    6
    """
    return 0 if x is None else x.head + add(x.tail)


def contains(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains(L(1, L(2, L(3, None))), 4)
    False
    >>> contains(L(1, L(2, L(3, None))), 2)
    True
    """
    if x.tail is None:
        return False
    return True if e == x.head else contains(x.tail,e)
#complexity is worst case O(n) and best case O(1)?
# match x:
#     case None: return Flase
#     case L(head,_) if head==e : retrun True
#     case L(_,tail): return contains(tail,e)



def drop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop(x, 3)
    L(4, None)
    >>> drop(x,5)
    None
    """
    if k  <= length(x): 
        if k==0:
            return x
        else:
            i=k-1
        return drop(x.tail,i) # this cannot be the most beautiful way, displeasing
    else:
        return None
    # match (x,k):
    #     case (None,_): return False
    #     case (_,0): return x
    #     case (L(_,tail),k): return drop(tail,k-1)
    # Complexity: 

def keep(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep(x, 0) # returns None but doesn't print
    >>> keep(x, 1)
    L(1, None)
    >>> keep(x, 3)
    L(1, L(2, L(3, None)))
    """
    i=k
    if k <= length(x):
        if k==0:
            return None
        else:
            i -= 1
            return(L(x.head,keep(x.tail,i)))
    # match (x,k):
    #     case (None,_): return None
    #     case (_,0): return None
    #     case(L(head,tail),k): return L(head,keep(tail,k-1)
    # Complexity

def concat(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    if x.tail is None:
        return L(x.head, y)
    else:
        return L(x.head, concat(x.tail,y))
    ...
    # match x:
    #     case None: return y
    #     case L(head,tail): return L(head,concat(tail,y))

def append(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    if x.tail is None:
        return L(x.head,L(e,None))
    else:
        return L(x.head, append(x.tail,e))


def rev(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    #ARRRRRGHHHHH
    # u = L()
    # if x.tail is None:
    #     return 'idiot'
    # else:
    #did i give up... oh yes
    # match x:
    #     case None: return None
    #     case L(head,tail): return append(rev(tail),head)
    

# Tail-recursive versions ###########################################


def length_tr(x: List[T], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> length_tr(None)
    0
    >>> length_tr(L(1, None))
    1
    >>> length_tr(L(1, L(2, L(3, None))))
    3
    """
    return acc if x is None else length_tr(x.tail, acc + 1)
    # match x:
    #     case None: return acc
    #     case L(_,tail): return length_tr(tail,acc+1)

def add_tr(x: List[int], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> add_tr(None)
    0
    >>> add_tr(L(1, None))
    1
    >>> add_tr(L(1, L(2, L(3, None))))
    6
    """
    return acc if x is None else add_tr(x.tail, acc + x.head)
    # match x:
    #     case None: return acc
    #     case L(head,tail): return add_tr(tail,acc+head)

def contains_tr(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_tr(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_tr(L(1, L(2, L(3, None))), 2)
    True
    """
    return False if x.tail is None else x.head==e or contains_tr(x.tail,e) # is this tail recursion??! not too sure
    ...
    # match x:
    #     case None: return False
    #     case L(head,_) if head==e: return True



def drop_tr(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_tr(x, 3)
    L(4, None)
    """
    return x if k==0 else drop_tr(x.tail,k-1)  # the definition of tail recursion is a little iffy to me
    # match (x,k):
    #     case (x,0): return x
    #     case L(None, _): return None
    #     case (L(_,tail),k): return drop_tr(tail,k-1)



def keep_tr(x: List[T], k: int, acc: List[T]) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep_tr(x, 0) # returns None but doesn't print
    >>> keep_tr(x, 1)
    L(1, None)
    >>> keep_tr(x, 3)
    L(1, L(2, L(3, None)))
    """
    # match (x,k):
    #     case (_,0): return rev(acc)
    #     case (None,_): return rev(acc)
    #     case(L(head,tail),k): return keep_tr(tail,k-1,L(head,acc))


# def _flip(x,y):
#     match y:
#         case None: return x
#         case L(head,tail): return _flip(L(head,x),tail)
        


def concat_tr(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_tr(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    #return L(x.head,y) if x.tail is None else L(x.head,concat_tr(x.tail,y))
    return _flip(y,rev_tr(x))

# def _flip(x,y):
#     match y:
#         case None: return x
#         case L(head,tail): return _flip(L(head,x),tail)
        

def append_tr(x: List[T], e: T, acc: List[T]) -> List[T]:
    """
    Append e to x.

    >>> append_tr(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    #return L(x.head,L(e,None)) if x.tail is None else L(x.head, append_tr(x.tail,e))
    return concat_tr(x, L(e,None))

def rev_tr(x: List[T], acc= List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev_tr(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    # match x:
    #     case None: return acc
    #     case L(head,tail): return rev_tr(tail,L(head,acc))


# Loop versions ###########################################

def length_loop(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length_loop(None)
    0
    >>> length_loop(L(1, None))
    1
    >>> length_loop(L(1, L(2, L(3, None))))
    3
    """
    acc = 0
    while x:
        acc += 1
        x = x.tail
    return acc


def add_loop(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> add_loop(None)
    0
    >>> add_loop(L(1, None))
    1
    >>> add_loop(L(1, L(2, L(3, None))))
    6
    """
    acc = 0
    while x:
        acc += x.head
        x = x.tail
    return acc
    # the directly translated stuff: would probaly correspond to:
    # tail recursive:
    # match x:
    #     case None: return acc
    #     case L(head,tail): return add_tr(tail,acc+head)
    # easy always work stuff: 
    # while x is not None:
    #     x.head, acc = x.tail, acc+x.head
    # return acc

#pointers to self:
# to translate tail recursion to loops:
# 1) make simple while loop:
# 2) update variables to remove recursion
# 3) update while loop to contain None cases and such
# 4) Done, simple and workable 


def contains_loop(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_loop(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_loop(L(1, L(2, L(3, None))), 2)
    True
    """
    acc=0
    while x:
        if x.head==e:
            acc += 1
        x = x.tail
    return acc != 0
    ...
    # tail recursion version:
    # match x:
    #     case None: return False
    #     case L(head,_) if head==e: return True
    # loop version:
    # while x is not None:
    # acc=0
    #     if x.head == e:
    #         acc +=1
    # return acc != 0


def drop_loop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_loop(x, 3)
    L(4, None)
    """
    if k==0:
        return x
    while k:
        x=x.tail
        k -= 1
    return x
# tail recursive and translated: 
#   # match (x,k):
    #     case (x,0): return x
    #     case L(None, _): return None
    #     case (L(_,tail),k): return drop_tr(tail,k-1)
# translated:
# while k!=0 and x is not None:
#   x, k = x.tail, k-1
# return x

def _flip_loop(x,y):
    while y is not None:
            x,y = L(y.head,x),y.tail
    return x

def rev_loop(x: List[T]) -> List[T]:
    """
    Reverse a list.
    >>> rev_loop(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    return _flip_loop(None,x)


def keep_loop(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep_loop(x, 0) # returns None but doesn't print
    >>> keep_loop(x, 1)
    L(1, None)
    >>> keep_loop(x, 3)
    L(1, L(2, L(3, None)))
    """
    acc: List[T] = None
    while k != 0 and x is not None:
            x, k, acc = x.tail,k-1,L(x.head,acc)
    return rev_loop(acc)


def concat_loop(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_loop(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    return _flip_loop(y,rev_loop(x))



def append_loop(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append_loop(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    ...
    return concat_loop(x, L(e,None))

