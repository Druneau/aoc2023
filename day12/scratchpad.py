from day12 import Consume


def test_arrangements_from_record():

    # -  ???.###   3? 3# 1.  REMOVED 0  SumSprings=5 Chars=7
    assert Consume.arrangements_from_record(
        '???????', [1, 1, 3]) == 1

    # -  .??..??...?##. 5?  2#  7.   REMOVED 6  SumSprings=5 Chars=14
    assert Consume.arrangements_from_record(
        '????????', [1, 1, 3]) == 4

    # -  ?#?#?#?#?#?#?#?  8? 7# 0.  REMOVED 1  SumSprings=11 Chars=15
    assert Consume.arrangements_from_record(
        '??????????????', [1, 3, 1, 6]) == 1

    # -  ????.#...#...
    # -  ????.#...#... 4? 2# 7.  REMOVED 5  SumSprings= 6 Chars=13
    assert Consume.arrangements_from_record(
        '????????', [4, 1, 1]) == 1

    # -  ????.######..#####. 4?  11#  4.  REMOVED 4  SumSprings=12 Chars=19
    assert Consume.arrangements_from_record(
        '???????????????', [1, 6, 5]) == 4

    # -  ?###????????   9?  3#  0.  REMOVED 2  SumSprings=6 Chars=12
    assert Consume.arrangements_from_record(
        '??????????', [3, 2, 1]) == 10

    # -  ..?##?##??????#? 7,5  distance between existing #'? == 11
    # assert Consume.arrangements_from_record(
    #    '??????????????', [7, 5]) == 2

    # trim leading AND trailing .'s
    # adjust for required .'s base on number of items.
    # crunch
    # victory???

    # -  ??#?.??#????? 1,2,3,2  10?  2#  1.
    assert Consume.arrangements_from_record(
        '??#?', [1, 2]) == 1
    assert Consume.arrangements_from_record(
        '????????', [3, 2]) == 6
    assert Consume.arrangements_from_record(
        '????.????????', [1, 2, 3, 2]) == 6
    assert Consume.arrangements_from_record(
        '????.????????', [1, 2, 3, 2]) == 6

   # new new new final strategy!!!

   # consume and solve until not possible
   # look at groups of ###'s and match to groups.  remove if perfect match
   # check length required by springs and length of subgroups.  should be able to
   #   send to solver based on those groups.
   # branch if overlaps?
