% Example script for the parcellation pipeline
% Note: This is a representative example of the extraction pipeline.
% Specific adaptations were made for each dataset regarding directory 
% structures, multiple runs, and subject naming conventions.
%
% Requirements: SPM12 must be added to the path.

clc;
clear;

% Define paths
script_dir = fileparts(mfilename('fullpath'));
main_dir = fileparts(fileparts(script_dir));

spm_path = '/path/to/spm12'; % update this path

% Select Dataset and Atlas Mask
dataset = 'DATASET_NAME'; 
atlas_name = 'AAL'; 

% Initialization
addpath(script_dir); 
if exist(spm_path, 'dir')
    addpath(spm_path);
else
    disp('Warning: SPM12 path not found.');
end

% Load Mask
mask_file = fullfile(script_dir, 'masks', atlas_name, [atlas_name, '.nii']);
if exist(mask_file, 'file')
    mask_hdr = spm_vol(mask_file);
    mask_data = spm_read_vols(mask_hdr);
end

% Example subject list and conditions
sub_list = [1, 2, 3]; 
conditions = {'COND1', 'COND2'};
runs = 1:3;

output_dir = fullfile(main_dir, 'results', 'func_networks', atlas_name, dataset);
if ~exist(output_dir, 'dir')
    mkdir(output_dir);
end

% Main extraction loop
for iSess = 1:length(sub_list)
    sub_id = sprintf('sub-%03d', sub_list(iSess));
    
    for iCond = 1:length(conditions)
        cond_name = conditions{iCond};
        
        for iRun = runs
            raw_func_dir = fullfile(main_dir, 'data', 'raw', sub_id, ['ses-', cond_name], 'func');
            nii_filename = sprintf('%s_ses-%s_task-rest_run-%02d_bold.nii.gz', sub_id, cond_name, iRun);
            nii_filepath = fullfile(raw_func_dir, nii_filename);
            
            if ~exist(nii_filepath, 'file')
                fprintf('Skipping missing file: %s\n', nii_filename);
                continue;
            end
            
            fprintf('Extracting %s %s R%d...\n', sub_id, cond_name, iRun);
            
            bold_hdr = spm_vol(nii_filepath);
            bold_data = spm_read_vols(bold_hdr);
            
            func_roi = bold_to_networks(bold_data, mask_data);
            
            out_sub_dir = fullfile(output_dir, sub_id, cond_name);
            if ~exist(out_sub_dir, 'dir')
                mkdir(out_sub_dir);
            end
            
            out_filename = sprintf('%s_ses-%s_task-rest_run-%02d_bold_%s.mat', sub_id, cond_name, iRun, atlas_name);
            save(fullfile(out_sub_dir, out_filename), 'func_roi');
        end
    end
end
