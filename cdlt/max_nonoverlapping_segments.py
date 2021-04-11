def solution(A, B):
    segments=[]
    for a,b in zip(A,B):
        segments.append([a,b])
    segments.sort(key=lambda _: (_[1],_[0]))
    previous_segment=segments[0]
    segment_count=1
    for segment in segments[1:]:
        if segment[0]>previous_segment[1]:
            segment_count+=1
            previous_segment=segment
    return segment_count
