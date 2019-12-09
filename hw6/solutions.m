% Luke Hartman
% Work done for hw6

problem2_3_4()
problem5()

function p3 = problem2_3_4() 
    % make G
    P = [
        1 0 0 0 1 0;
        1 0 0 0 0 1;
        0 1 0 0 1 0;
        0 1 0 0 0 1;
        0 0 1 0 1 0;
        0 0 1 0 0 1;
        0 0 0 1 1 0;
        0 0 0 1 0 1
    ];
    G = [ eye(8) P];
    
    % build M
    M = zeros(256, 8);
    for i = [0:255]
        num = flip(de2bi(i));
        dims = size(num);
        new_row = horzcat(zeros(1, 8 - dims(2)), num);
        M(i+1,:) = new_row;
    end
    
    % find C
    C = mod(M*G, 2);
    
    % 3. lookup codeword [1 1 1 1 0 0 0 1 0 0 0 1 0 1]
    codeword1 = [1 1 1 1 0 0 0 1 0 0 0 1 0 1];
    [~,index] = ismember(codeword1, C,'rows');
    
    % 4. lookup codeword [1 1 0 0 1 1 1 0 0 0 1 1 0 0]
    codeword2 = [1 1 0 0 1 1 1 0 0 0 1 1 0 0];
    [~,index] = ismember(codeword2, C,'rows');
    % index is equal to 0, so this one is not valid
    % looks like we're gonna have to do some syndrome stuff
    H = [ transpose(P) eye(6)];
    s = mod(codeword2 * transpose(H), 2)
    % s =  0     0     1     0     1     0
    % this means m_5 is an error so flip appropriate bit and look up new
    % codeword
    codeword2fixed = [1 1 0 0 0 1 1 0 0 0 1 1 0 0];
    [~,index] = ismember(codeword2fixed, C,'rows');
    % received word corrects to codeword at position 199
    C(index, :);
    % C(index, :) = [1 1 0 0 0 1 1 0 0 0 1 1 0 0]
end

function p5 = problem5()
    P = [
        0 0 0 0 0;
        0 1 0 1 0;
        0 0 1 1 0;
        0 1 1 0 0;
        0 0 0 0 1;
        0 1 0 1 1;
        0 0 1 1 1;
        0 1 1 0 1;
    ];
    G = [P eye(8)];
    H = [eye(5) transpose(P)];
    mod(G*transpose(H), 2)
    
end