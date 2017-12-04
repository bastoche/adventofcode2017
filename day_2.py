def part_one(input):
    return sum([max_difference(line) for line in parse(input)])


def max_difference(numbers):
    return max(numbers) - min(numbers)


def parse(input):
    return [to_number_list(line) for line in input.splitlines()]


def to_number_list(list):
    return [int(element) for element in list.split()]


def part_two(input):
    return sum([max_even_division_result(all_pairs(line)) for line in parse(input)])


def max_even_division_result(pairs):
    return max([even_division_result(left, right) for left, right in pairs])


def even_division_result(left, right):
    smallest = min(left, right)
    largest = max(left, right)
    if largest % smallest == 0:
        return largest // smallest
    return 0


def all_pairs(list):
    length = len(list)
    result = []
    for i in range(length):
        for j in range(i + 1, length):
            result.append((list[i], list[j]))
    return result


if __name__ == "__main__":
    input = """86	440	233	83	393	420	228	491	159	13	110	135	97	238	92	396
3646	3952	3430	145	1574	2722	3565	125	3303	843	152	1095	3805	134	3873	3024
2150	257	237	2155	1115	150	502	255	1531	894	2309	1982	2418	206	307	2370
1224	343	1039	126	1221	937	136	1185	1194	1312	1217	929	124	1394	1337	168
1695	2288	224	2667	2483	3528	809	263	2364	514	3457	3180	2916	239	212	3017
827	3521	127	92	2328	3315	1179	3240	695	3144	3139	533	132	82	108	854
1522	2136	1252	1049	207	2821	2484	413	2166	1779	162	2154	158	2811	164	2632
95	579	1586	1700	79	1745	1105	89	1896	798	1511	1308	1674	701	60	2066
1210	325	98	56	1486	1668	64	1601	1934	1384	69	1725	992	619	84	167
4620	2358	2195	4312	168	1606	4050	102	2502	138	135	4175	1477	2277	2226	1286
5912	6261	3393	431	6285	3636	4836	180	6158	6270	209	3662	5545	204	6131	230
170	2056	2123	2220	2275	139	461	810	1429	124	1470	2085	141	1533	1831	518
193	281	2976	3009	626	152	1750	1185	3332	715	1861	186	1768	3396	201	3225
492	1179	154	1497	819	2809	2200	2324	157	2688	1518	168	2767	2369	2583	173
286	2076	243	939	399	451	231	2187	2295	453	1206	2468	2183	230	714	681
3111	2857	2312	3230	149	3082	408	1148	2428	134	147	620	128	157	492	2879"""
    print(part_one(input))
    print(part_two(input))