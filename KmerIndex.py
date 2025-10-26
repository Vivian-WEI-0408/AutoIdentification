from collections import defaultdict



#由于数据库不同，所以Seq_id存储值为Seq_name

class KmerIndex:
    def __init__(self,k=10):
        self.k = k
        self.index = defaultdict(list)
    
    def add_sequence(self,seq_id,sequence):
        seq_len = len(sequence)

        if seq_len < self.k:
            return
        
        for i in range(seq_len - self.k +1):
            kmer = sequence[i:i+self.k]
            self.index[kmer].append((seq_id,i))

    def query(self,sequence, min_matches=5):
        matches = defaultdict(list)
        query_len = len(sequence)

        for i in range(query_len - self.k+1):
            kmer = sequence[i:i+self.k]
            for seq_id,pos in self.index.get(kmer,[]):
                offset = pos -i
                matches[(seq_id, offset)].append(i)
        
        significant_matches = []
        for (seq_id,offset), positions in matches.items():
            match_count = len(positions)
            if match_count >= min_matches:
                density = match_count/(max(positions) - min(positions)+self.k) if len(positions)>1 else 1
                significant_matches.append({'seq_id':seq_id,
                                            'offset':offset,
                                            'match_count':match_count,
                                            'density':density,
                                            'start':min(positions),
                                            'end':max(positions)+self.k})
        significant_matches.sort(key=lambda x:x['match_count'],reverse=True)
        return significant_matches[:100]