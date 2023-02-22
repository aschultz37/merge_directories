## Purpose  
Given a directory (super-directory) containing sub-directories, merges files from multiple 
sub-directories into another (single) sub-directory.  
Files will be renamed according to their source sub-directory to avoid name conflicts.  
  
## Function  
Takes a pattern to find in directory names.  
Merges all files in matching directories into a directory of the pattern's name.  
Files from each directory are copied and their names prefixed with the directory name.  
  
## Usage  
- Prompt for super-directory: Enter the full path to the directory containing sub-directories that you want to merge.  
- Prompt for pattern: Ensure this pattern is unique to the directories you want. Length otherwise unimportant.  
- To quit, enter 'quit' when prompted for pattern.  
  
## Usage Notes
- Requires script to be outside the super-directory.  
- Super-directory should contain _only_ directories (no files).