In general, this design should be a very standard skeleton design for an image processing pipeline. Images and their metadata are pushed from the kafka stream and stored in their respective storage.

Images are then processed by interminary application and the results or output of the process are stored into the data warehouse, same goes the image metadata.

Images will be moved to a cold storage archive if they need to be stored, but not access as frequently.

The assumption for this design 
*  The file size for all images will not vary too much.
*  The image will not need to be view/retrieve after user has submitted it.
* Assume there might be a situation where image needs to be stored for a very long amount of time


## pros
Scalable
Adding redundant blocks for the DB/Storage

## cons
Build for a very specific use case, might not be flexible enough for a different type of data.