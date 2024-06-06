def is_valid_chess_board(board_dict):
    # 駒のカウントを初期化
    black_king_count = 0
    white_king_count = 0
    black_piece_count = 0
    white_piece_count = 0
    black_pawn_count = 0
    white_pawn_count = 0
    
    # 駒の種類のリスト
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
    # 駒の位置をチェック
    for position, piece in board_dict.items():
        # 有効な位置かどうかをチェック
        if not (len(position) == 2 and position[0].isdigit() and '1' <= position[0] <= '8' and position[1].isalpha() and 'a' <= position[1] <= 'h'):
            return False
        
        # 駒の名前が適切かどうかをチェック
        if not (piece.startswith('w') or piece.startswith('b')):
            return False
        piece_type = piece[1:]
        if piece_type not in valid_pieces:
            return False
        
        # 駒のカウント
        if piece.startswith('b'):
            black_piece_count += 1
            if piece_type == 'king':
                black_king_count += 1
            if piece_type == 'pawn':
                black_pawn_count += 1
        elif piece.startswith('w'):
            white_piece_count += 1
            if piece_type == 'king':
                white_king_count += 1
            if piece_type == 'pawn':
                white_pawn_count += 1
    
    # チェスボードの条件をチェック
    if black_king_count == 1 and white_king_count == 1 and black_piece_count <= 16 and white_piece_count <= 16 and black_pawn_count <= 8 and white_pawn_count <= 8:
        return True
    else:
        return False

# チェスボードの辞書
chess_board_dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h':'bqueen', '3e': 'wking'}

# チェスボードが正しいかどうかを確認
print(is_valid_chess_board(chess_board_dict))  # 出力: True
