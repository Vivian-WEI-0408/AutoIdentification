from Bio import Restriction
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


'''
Scar  标识
GTGC   A
ATCA   A*
AATG   B
TAAA   C
CCTC   D
GCTT   E
CTGA   F
CTGA   F
TACG   G
TTCC   H
AGGT   I
TGTC   K
'''

type2s_enzymes = ["BsmBI","BsaI","BbsI","AarI","SapI"]
class ScarIdentify:
    def __init__(self, Sequence):
        self.Sequence = Sequence
        self.Part = SeqRecord(Seq(self.Sequence),id="test",name="test",description="test")
    
    def number_of_site(self,enzyme):
        linear = False
        return enzyme.search(self.Part.seq,linear=linear)

    def enzyme_fit_score(self,enzyme_name):
        enzyme = Restriction.__dict__[enzyme_name]
        Site = self.number_of_site(enzyme)
        if(len(Site) == 2):
            scar = {"start":self.Part.seq[Site[0]-1:Site[0]+3],"end":self.Part.seq[Site[1]-1:Site[1]+3]}
        else:
            scar = {"start":"","end":""}
        return {"enzyme_name":enzyme, "site_number":len(Site),"Scar":scar}
        # return self.number_of_site(enzyme)

def scarFunction(seq):

    SI = ScarIdentify(seq)
    scar_list = []
    for enzyme in type2s_enzymes:
        NoSite = SI.enzyme_fit_score(enzyme)
        scar_str = ""
        if(NoSite['site_number'] == 2):
            if(NoSite["Scar"]["start"].upper() == "GCTT"):
                scar_str += "E"
            elif(NoSite["Scar"]["start"].upper() == "CTGA"):
                scar_str += "F"
            elif(NoSite["Scar"]["start"].upper() == "TACG"):
                scar_str += "G"
            elif(NoSite["Scar"]["start"].upper() == "TTCC"):
                scar_str += "H"
            elif(NoSite["Scar"]["start"].upper() == "GTGC"):
                scar_str += "A"
            elif(NoSite["Scar"]["start"].upper() == "ATCA"):
                scar_str += "A*"
            elif(NoSite["Scar"]["start"].upper() == "AATG"):
                scar_str += "B"
            elif(NoSite["Scar"]["start"].upper() == "TAAA"):
                scar_str += "C"
            elif(NoSite["Scar"]["start"].upper() == "CCTC"):
                scar_str += "D"
            if(NoSite["Scar"]["end"].upper() == "CTGA"):
                scar_str += "F"
            elif(NoSite["Scar"]["end"].upper() == "TACG"):
                scar_str += "G"
            elif(NoSite["Scar"]["end"].upper() == "TTCC"):
                scar_str += "H"
            elif(NoSite["Scar"]["end"].upper() == "AGGT"):
                scar_str += "I"
            elif(NoSite["Scar"]["end"].upper() == "TGTC"):
                scar_str += "K"
            elif(NoSite["Scar"]["end"].upper() == "CCTC"):
                scar_str += "D"
            elif(NoSite["Scar"]["end"].upper() == "GTGC"):
                scar_str += "A"
            elif(NoSite["Scar"]["end"].upper() == "ATCA"):
                scar_str += "A*"
            elif(NoSite["Scar"]["end"].upper() == "AATG"):
                scar_str += "B"
            elif(NoSite["Scar"]["end"].upper() == "TAAA"):
                scar_str += "C"
        if(scar_str == ""):
            scar_list.append("NO SITE")
        else:
            scar_list.append(scar_str)
    return scar_list