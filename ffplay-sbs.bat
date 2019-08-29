set left=model1_clip39370_256x256_30_141_qp18.mp4
set right=model2_clip39370_256x256_30_141_qp18.mp4
ffplay -f lavfi "movie=%left%,scale=iw/2:ih[v0];movie=%right%,scale=iw/2:ih[v1];[v0][v1]hstack"
