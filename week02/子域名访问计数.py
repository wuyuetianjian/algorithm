class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        resdic = dict()
        result = []
        for i in cpdomains:
            x = i.split()
            n = x[1].split(".")
            p = ""
            for m in range(0, len(n)):
                if p == "":
                    p = p + n[-m-1]
                else:
                    p = n[-m-1] + "." + p
                if p not in resdic.keys():
                    resdic[p] = int(x[0])
                else:
                    resdic[p] = resdic[p] + int(x[0])
        for q in resdic.keys():
            result.append(f"{resdic[q]} {q}")
        return result