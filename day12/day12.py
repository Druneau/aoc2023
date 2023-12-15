from itertools import accumulate
from math import prod


class Consume:
    @staticmethod
    def question(record, springs, arrangements=1):
        if not record and not springs:
            return Consume.if_return(record, springs, arrangements)

        if record == len(record)*record[0]:
            # all ???????  solve and return answer
            arr = Consume.arrangements_from_record(record, springs)
            return Consume.if_return('', [], arr*arrangements)
        if len(springs) == 1:
            # '??###?? 3'
            hashtags = record.strip('?')
            if len(hashtags) == springs[0]:
                return Consume.if_return('', [], arrangements)
        if '.' in record:
            # split and try to match groups of springs to groups of ?#?#?#?#'s
            # build a list of thing to run in one shot.  some migh have duplicate and be a branch off.

            records = list(filter(None, record.split('.')))
            a = arrangements

            for r in records:
                l_r = len(r)
                fits = []
                for s in springs:
                    if sum(fits) + s > (l_r - (len(fits))):
                        break
                    fits.append(s)
                springs = springs[len(fits):]
                _, _, a1 = Consume.recursive(r, fits, a)
                a *= a1

            return Consume.if_return('', [], a1)

        if record.startswith('?#'):
            # are we lucky and can just consume?
            spring = springs[0]
            perfect_start = '?' + spring*'#'
            if record.startswith(perfect_start):
                springs = springs[1:]
                record = record[len(perfect_start)+1:]
                r, s, a = Consume.recursive(record, springs, arrangements)
                return Consume.if_return(r, s, a*arrangements)
            # we need to branch? e.g. ?#?#?????? 6 is two arrangements possible

        return ('', [], -1)

    @staticmethod
    def period(record, springs, arrangements=1):
        if not record and not springs:
            return Consume.if_return(record, springs, arrangements)

        if record.startswith('.'):
            while record.startswith('.'):
                record = record[1:]

        if record.endswith('.'):
            while record.endswith('.'):
                record = record[:-1]

        return Consume.if_return(record, springs, arrangements)

    @staticmethod
    def hashtag(record, springs, arrangements=1):
        if not record and not springs:
            return Consume.if_return(record, springs, arrangements)

        if record.startswith('#'):
            spring = springs[0]
            springs = springs[1:]
            chars_to_remove = spring + 1  # remove trailing '.'
            record = record[chars_to_remove:]

        if record.endswith('#'):
            spring = springs[-1]
            springs = springs[:-1]
            chars_to_remove = spring + 1  # remove leading '.'
            record = record[:-chars_to_remove]

        if not springs:
            record = ''

        return Consume.if_return(record, springs, arrangements)

    @staticmethod
    def if_return(record, springs, arrangements):
        return (record, springs, arrangements)

    @staticmethod
    def accumulate_level(length, levels):
        base = range(1, length+1)
        for i in range(levels-1):
            base = accumulate(base)
        return list(base)

    @staticmethod
    def arrangements(extra_space, spring_groups):
        return Consume.accumulate_level(extra_space+1, spring_groups)[-1]

    @staticmethod
    def arrangements_from_record(record, springs):
        items = len(springs)
        items_spaces = sum(springs)
        required_periods = items - 1
        extra_spaces = len(record)-items_spaces-required_periods

        return Consume.arrangements(extra_spaces, items)

    @staticmethod
    def recursive(record, springs, arrangements=1):

        record, springs, arrangements = Consume.period(
            record, springs, arrangements)

        record, springs, arrangements = Consume.hashtag(
            record, springs, arrangements)

        record, springs, arrangements = Consume.question(
            record, springs, arrangements)

        # if we make it here we're done?
        return Consume.if_return(record, springs, arrangements)


def part1(input='day12/input.txt'):
    with open(input, 'r') as file:
        for line in file:
            print('Started:{}'.format(line.strip()))
            record, springs = line.split()
            springs = [int(x) for x in springs.split(',')]
            _, _, arrangements = Consume.recursive(record, springs)

            if arrangements == -1:
                print('Failed:{}'.format(line.strip()))
            else:
                print('{} {} : {}'.format(record, springs, arrangements))

    return 1


if __name__ == '__main__':
    part1()
